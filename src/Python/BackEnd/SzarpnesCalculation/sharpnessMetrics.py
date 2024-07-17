import numpy
from skimage import filters, color, feature
import cv2


def image_sharpness(img):
    m = numpy.mean(img)
    img_s = numpy.add(-m, img)
    img_sq = numpy.multiply(img_s, img_s)
    r = numpy.sum(img_sq)
    return r


def image_sharpness2(img):
    img_s = numpy.gradient(img)
    img_sq = numpy.abs(img_s)
    r = numpy.sum(img_sq)
    return r


def sobel(img):
    return numpy.var(filters.sobel(img))


def fft_based_sharpness(image):
    f = numpy.fft.fft2(image)
    fshift = numpy.fft.fftshift(f)
    magnitude_spectrum = 20 * numpy.log(numpy.abs(fshift))
    return numpy.var(magnitude_spectrum)


def scharr_variance(image):
    return numpy.var(filters.scharr(image))


def edge_based_sharpness(image, *args):
    edges = cv2.Canny(image, 100, 200)
    return numpy.var(edges)


def lpc_based_sharpness(image):
    h, w = image.shape
    coherence_sum = 0
    for i in range(0, h - 15, 16):
        for j in range(0, w - 15, 16):
            patch = image[i:i + 16, j:j + 16]
            # Calculate gradient
            grad_x = cv2.Sobel(patch, cv2.CV_64F, 1, 0, ksize=3)
            grad_y = cv2.Sobel(patch, cv2.CV_64F, 0, 1, ksize=3)
            # Calculate local phase
            phase = numpy.arctan2(grad_y, grad_x)
            coherence_sum += numpy.abs(numpy.sum(numpy.exp(phase * 1j))) / numpy.sqrt(
                numpy.sum(numpy.abs(numpy.exp(phase * 1j)) ** 2))
    return coherence_sum / ((h // 16) * (w // 16))
