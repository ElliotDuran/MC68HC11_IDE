# !/usr/bin/env python


def get_code(file):
    """
    This function takes a program with an ".asc" extension
    and generates a list with the contents of the program

    :param file: name of the program to be compiled
    :return: a list of each line of code with no spaces and comments
    """

    aux = []
    code_list = []

    try:
        asc_file = open(file, 'r')
        program_lines = asc_file.readlines()

        for idx in range(len(program_lines)):
            line = program_lines[idx].replace(' ', '@').strip()

            if line == '\n' or len(line) == 0:
                aux.append('/n')
            elif line.find('@') != 0 and line.find('*') != 0 \
                    and "EQU" not in line and "FCB" not in line:
                aux.append(line.replace('@', '').strip())
            else:
                aux.append(line.replace('@', '').strip())

        for idx in range(len(aux)):
            asterisk = aux[idx].find('*')

            if asterisk > -1 and asterisk != 0:
                without_comments = aux[idx][:asterisk]
                code_list.append(without_comments)
            elif asterisk == 0:
                code_list.append('*')
            else:
                code_list.append(aux[idx])

        asc_file.close()

    except IOError:
        pass

    return code_list


if __name__ == "__main__":
    var = get_code(r'C:\Users\ellio\Documents\Proyectos_VS_Code\IDE_MC68HC11\Programs\arch.asc')
    print(var)
