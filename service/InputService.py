def process_input(input):
    to_process = input['input']

    upper_case = to_process.upper()

    with_space = ''

    if "-" or "_" in to_process:
        with_space = to_process.replace('-', ' ').replace('_', ' ').replace('&', 'AND')
    return {'uppercase': upper_case, 'with_space': with_space}, 201
