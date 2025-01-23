# User Manual
## General Instructions

### Marking ROI:

#### Select ROI Type:

From the context menu, choose the type of ROI:
* Hand Mode: Prevents accidental ROI creation
* Classic Mode: Allow marking of standard rectangular rois and point rois by pressing and dragging.
* Corner Mode: Allow marking of standard rectangular rois by marking its corners
* Calculate distant between points: Allow for creating lines that present distant between selected points on the sample

By default, the Pointer Mode is selected.

![ROI_Type.png](Screenshot%2FROI_Type.png)


#### Mark the Desired ROI:

For rectangular ROIs:

- Drag the mouse from one corner to the opposite corner.
- Alternatively, select two opposite corners if "Corner Mode" is active.

For point ROIs:

- Click directly on the desired point.
    
![RoiCreation.gif](Screenshot%2FRoiCreation.gif)

ROI context menu:

Right-click on an ROI to open its context menu, where you can:
- Center the view on the ROI.
- Edit its size by dragging its edges.
- Rename or delete the ROI.

![RoiEdit.gif](Screenshot%2FRoiEdit.gif)

![PointEdit.gif](Screenshot%2FPointEdit.gif)

![ReName.gif](Screenshot%2FReName.gif)

ROI List:

At the right edge of the program a list of marked ROIs is displayed.

Right-click on an entry in the list to open a context menu for editing the selected ROI.

![RoiList.gif](Screenshot%2FRoiList.gif)

Sample Manipulator Interactions

Step Size Configuration:
- Use the context menu under the manipulator settings to adjust step lengths.

Moving the Manipulator:
- Buttons in the bottom-right corner of the program window control movement.
- Right-click anywhere in the program window to display movement buttons near the cursor.
- Use WASD or arrow keys for manual movement.
- Center the view at a point via the right-click context menu.

Context Menu Options
File:
- Save ROI List: Opens a dialog to save marked ROIs to a file.
- Import ROI List: Opens a dialog to load a file containing marked ROIs.

Camera Settings:

- All Settings: Opens the camera manufacturer's settings window for image adjustments.
- Calibration: Initiates automatic calibration (requires a calibration matrix and is recommended only for technicians).
- Save Current Frame: Saves the current camera view to a file.
- Autofocus: Activates automatic image sharpening.

Manipulator:

- Home All Axes: Resets all manipulator axes to their zero positions.
- Go to Coordinates: Allows manual entry of target coordinates.
- Move by Value: Moves the manipulator by a specified distance (useful for long moves).
- Set Step Size: Configures the standard step size for small adjustments (deprecated).
- Calculation Inaccuracy: Measures and logs manipulator error. Recommended at the start and end of measurements.
- Remove Sample: Moves the manipulator to the best position for mounting/dismounting the sample matrix.
- Calculate Zero points: Determines the position of the sample matrix (run after mounting).

Mosaic:

- Show Mosaic: Displays the collected mosaic.
- Create Mosaic: Gathers images to create a mosaic.
- Save Mosaic: Save the mosaic to a file.
- Create Mosaic From Here: Allows creation of a small mosaic from a selected area.
- Show Border Lines: Toggles visibility of image boundaries in the mosaic.

Work Field:

- Create Work Field: Creates a custom area for mosaic collection.
- List Work Fields: Displays available areas for mosaics.

ROI:

- Hand Mode: Disables ROI marking.
- Classic Mode: Allows standard rectangular and point ROI marking.
- Corner Mode: Marks rectangular ROIs by selecting their corners.
- Calculate distant between points: allow to place a line mesurment on the sample viue

Starting Work
Quick Start Guide:

1. Launch the Program: Locate the PolSampleX icon or search for it in the file explorer and run it.
2. Move Manipulator to Sample Mounting Position:
    - The program will prompt you to confirm mounting a sample. After confirmation, the manipulator moves to the optimal position.
3. Mount the Sample Matrix: Secure the matrix using the included screws.
4. Select Working Zoom:
    - Observe the sample and choose the zoom level for marking ROIs.
5. Determine Matrix Position:
    - Run the subroutine to set the matrix position for the selected zoom.
6. Mark ROIs: Mark the areas or points of interest for measurement.

Recommended: Use a single zoom level.

Loading Marked ROIs

Quick Instructions:

1. Launch the Program: Locate and run the PolSampleX icon.
2. Move Manipulator to Sample Mounting Position:
    - Confirm mounting a sample when prompted.
3. Mount the Associated Sample Matrix: Secure it with screws and confirm in the program.
4. Determine Matrix Position:
    - Run the subroutine to align the matrix for the selected zoom.
5. Load ROI File:
    - From the "File" menu, select "Load ROI List".
    - Choose the associated file from the file explorer.