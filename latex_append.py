from __init__ import *

def appendPlot(latexFile, plotPrefix):

    imageName = plotPrefix
    split = plotPrefix.split(".")

    if (len(split)) == 2:
        imageName = split[0] + '_' + split[1]

    latexFile.write('\\begin{figure}[H]\n')
    latexFile.write('\t\\includegraphics[width=\\linewidth]{' + imageName + 'linear.png}\n')
    latexFile.write('\t\\caption{' + plotPrefix + ' Residual}\n')
    latexFile.write('\t\\label{' + imageName + 'linear}\n')
    latexFile.write('\\end{figure}\n')

    latexFile.write('\\begin{figure}[H]\n')
    latexFile.write('\t\\includegraphics[width=\\linewidth]{' + imageName + 'cont.png}\n')
    latexFile.write('\t\\caption{' + plotPrefix + ' Continuity}\n')
    latexFile.write('\t\\label{' + imageName + 'cont}\n')
    latexFile.write('\\end{figure}\n')

    latexFile.close()


def writeHeader(latexFile, latexFileName):
    split = latexFileName.split("_")
    titleOfLatexFile = split[0] + " " + split[1] + " Plots"
    titleOfLatexFile.title()
    latexFile.write('\\documentclass[12pt]{article}\n')
    latexFile.write('\\usepackage[utf8]{inputenc}\n')
    latexFile.write('\\usepackage{float}\n')
    latexFile.write('\\title{' + titleOfLatexFile + '}\n')
    latexFile.write('\\author{' + os.getlogin().title() + '}\n')
    latexFile.write('\\usepackage{natbib}\n')
    latexFile.write('\\usepackage{graphicx}\n')
    latexFile.write('\\begin{document}\n')
    latexFile.write('\\maketitle\n')


def writeFooter(latexFile):
    latexFile.write('\\end{document}\n')

'''
class LatexFileAppender:
    def __init__(self, latexFileName):
        self.latexFileName = latexFileName
        latexFile = open(latexFileName + '.tex', 'w')
        self.writeHeader(latexFile)
        latexFile.close()

    def appendPlot(self, plotPrefix):

        latexFile = open(self.latexFileName + '.tex', 'a')

        imageName = plotPrefix
        split = plotPrefix.split(".")

        if (len(split)) == 2:
            imageName = split[0] + '_' + split[1]

        latexFile.write('\\begin{figure}[H]\n')
        latexFile.write('\t\\includegraphics[width=\\linewidth]{' + imageName + 'linear.png}\n')
        latexFile.write('\t\\caption{' + plotPrefix + ' Residual}\n')
        latexFile.write('\t\\label{' + imageName + 'linear}\n')
        latexFile.write('\\end{figure}\n')

        latexFile.write('\\begin{figure}[H]\n')
        latexFile.write('\t\\includegraphics[width=\\linewidth]{' + imageName + 'cont.png}\n')
        latexFile.write('\t\\caption{' + plotPrefix + ' Continuity}\n')
        latexFile.write('\t\\label{' + imageName + 'cont}\n')
        latexFile.write('\\end{figure}\n')

        latexFile.close()

    def writeHeader(self, latexFile):
        latexFile.write('\\documentclass[12pt]{article}\n')
        latexFile.write('\\usepackage[utf8]{inputenc}\n')
        latexFile.write('\\usepackage{float}\n')
        latexFile.write('\\title{' + self.latexFileName + '}\n')
        latexFile.write('\\usepackage{natbib}\n')
        latexFile.write('\\usepackage{graphicx}\n')
        latexFile.write('\\begin{document}\n')
        latexFile.write('\\maketitle\n')

    def writeFooter(self, latexFile):
        latexFile.write('\\end{document}\n')

'''
