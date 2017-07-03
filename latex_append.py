from __init__ import *


def append_plot(latex_file, plot_prefix):
    """
    Adds plots in LaTeX file
    :param latex_file: File object which points to LaTeX file which is to be written
    :param plot_prefix: The plot's prefix
    :return: Nothing
    """
    image_name = plot_prefix
    split = plot_prefix.split(".")

    if (len(split)) == 2:
        image_name = split[0] + '_' + split[1]

    latex_file.write('\\begin{figure}[H]\n')
    latex_file.write('\t\\includegraphics[width=\\linewidth]{' + image_name + 'linear.png}\n')
    latex_file.write('\t\\caption{' + plot_prefix + ' Residual}\n')
    latex_file.write('\t\\label{' + image_name + 'linear}\n')
    latex_file.write('\\end{figure}\n')

    latex_file.write('\\begin{figure}[H]\n')
    latex_file.write('\t\\includegraphics[width=\\linewidth]{' + image_name + 'cont.png}\n')
    latex_file.write('\t\\caption{' + plot_prefix + ' Continuity}\n')
    latex_file.write('\t\\label{' + image_name + 'cont}\n')
    latex_file.write('\\end{figure}\n')

    latex_file.close()


def write_header(latex_file, latex_file_name):
    """
    Writes the header of LaTex file in which plots are to be saved
    :param latex_file: File object which points to LaTeX file which is to be written
    :param latex_file_name: Name of the LaTeX file
    :return: Nothing
    """

    # Title of LaTeX file
    split = latex_file_name.split("_")
    title_of_latex_file = split[0] + " " + split[1] + " Plots"
    title_of_latex_file.title()

    # Writing the header
    latex_file.write('\\documentclass[12pt]{article}\n')
    latex_file.write('\\usepackage[utf8]{inputenc}\n')
    latex_file.write('\\usepackage{float}\n')
    latex_file.write('\\title{' + title_of_latex_file + '}\n')
    latex_file.write('\\author{' + os.getlogin().title() + '}\n')
    latex_file.write('\\usepackage{natbib}\n')
    latex_file.write('\\usepackage{graphicx}\n')
    latex_file.write('\\begin{document}\n')
    latex_file.write('\\maketitle\n')


def write_footer(latex_file):
    """
    Writes the footer of LaTex file in which plots are to be saved
    :param latex_file: File object which points to LaTeX file which is to be written
    :return: Nothing
    """
    latex_file.write('\\end{document}\n')

