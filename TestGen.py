import inspect
import os


def main():
    src_dir = r'C:\Users\Zenbook\PycharmProjects\Magisterka\src'
    test_dir = r'C:\Users\Zenbook\PycharmProjects\Magisterka\tests'
    generate_unit_test_skeleton(src_dir, test_dir)


def generate_unit_test_skeleton(src_dir, test_dir):
    # Loop over all folders and files in src directory
    for root, dirs, files in os.walk(src_dir):
        # Get the relative path of the current folder or file
        relative_folder_path = os.path.relpath(root, src_dir)

        # Create the corresponding unit test folder in test directory
        test_folder = generate_test_folder_if_not_exists(relative_folder_path, test_dir)

        # Loop over all files in the current folder
        for file in files:
            # Check if the file has a .py extension
            if file.endswith('.py') and not  file.endswith('__init__.py'):
                generate_unit_tests_for_file(
                    file,
                    relative_folder_path,
                    test_folder,
                )


def generate_unit_tests_for_file(
    file,
    relative_directory,
    test_directory,
):
    # Create the corresponding unit test file in test directory
    generated_test_file_path = generate_unit_test_file(
        file,
        relative_directory,
        test_directory,
    )

    if generated_test_file_path is not None:
        # Get all classes and functions defined in the original file
        classes, functions = determine_members(file, relative_directory)

        # Generate test functions for each class and function
        generate_test_functions(
            file,
            generated_test_file_path,
            classes,
            functions,
        )


def generate_test_functions(
    file,
    test_file_path,
    classes,
    functions,
):
    module_name = determine_module_name(file)

    with open(test_file_path, 'a') as test_file:
        for class_name, class_instance in classes:
            generate_test_function_for_class(
                test_file,
                module_name,
                class_name,
                class_instance,
            )

        for function_name, function_instance in functions:
            generate_test_function_for_function(
                test_file,
                module_name,
                function_name,
                function_instance,
            )


def generate_test_function_for_function(
    test_file,
    module_name,
    function_name,
    function_instance,
):
    # Generate the test function name
    test_function_name = f'test_{function_name}'
    arguments = determine_arguments(function_instance)

    # Write the test function to the test file
    test_file.write(f'def {test_function_name}():\n')
    test_file.write(f'    # TODO: Implement test\n')
    test_file.write(f'    # result = {module_name}.{function_name}({arguments})\n')
    test_file.write(f'    pass\n')
    test_file.write('\n')


def generate_test_function_for_class(
    test_file,
    module_name,
    class_name,
    class_instance,
):
    # Generate the test function name
    test_function_name = f'test_{class_name}'

    arguments = determine_arguments(class_instance)

    # Write the test function to the test file
    test_file.write(f'def {test_function_name}():\n')
    test_file.write(f'    # TODO: Implement test\n')
    test_file.write(f'    # instance = {module_name}.{class_name}({arguments})\n')
    test_file.write(f'    pass\n')
    test_file.write('\n')


def determine_members(file, relative_directory):
    # Get the module name
    module_name = os.path.splitext(file)[0]

    # Import the module
    directory_import_path = relative_directory.replace('\\', '.')
    import_path = f'{directory_import_path}.{module_name}'
    module = __import__(import_path, fromlist=[module_name])

    # Get all classes and functions defined in the module
    classes = inspect.getmembers(module, inspect.isclass)
    functions = inspect.getmembers(module, inspect.isfunction)
    return classes, functions


def determine_arguments(function_instance):
    try:
        signature = inspect.signature(function_instance)
    except ValueError:
        return ''

    parameters = signature.parameters

    arguments = []
    for param in parameters.values():
        argument = determine_argument(param)
        arguments.append(argument)

    argument_string = ', '.join(arguments)
    if len(arguments) > 2:
        argument_string += ','  # leading comma causes line breaks if formatted with black
    return argument_string


def determine_argument(param):
    argument = param.name
    if param.default != inspect.Parameter.empty:
        default_value = determine_default_value(param.default)
        argument += f'={default_value}'
    return argument


def determine_default_value(default_instance):
    if inspect.isfunction(default_instance):
        return default_instance.__name__
    elif isinstance(default_instance, str):
        return f"'{default_instance}'"
    else:
        return default_instance


def generate_unit_test_file(file, relative_directory, test_directory):
    test_file_path = os.path.join(test_directory, f'test_{file}')
    if os.path.exists(test_file_path):
        return None
    else:
        # Open the test file in write mode
        with open(test_file_path, 'w') as f:
            # Write the initial import statement
            import_statement = generate_import_statement(file, relative_directory)
            f.write(import_statement)
            f.write('\n')
    return test_file_path


def generate_import_statement(file, relative_directory):
    directory_import_path = relative_directory.replace("\\", '.')
    module_name = determine_module_name(file)
    statement = f'from {directory_import_path} import {module_name}\n'
    return statement


def determine_module_name(file):
    name = os.path.splitext(file)[0]
    return name


def generate_test_folder_if_not_exists(relative_path, test_dir):
    test_folder = os.path.join(test_dir, relative_path)
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    return test_folder


if __name__ == '__main__':
    main()