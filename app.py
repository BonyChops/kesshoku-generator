from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm

import getpass


print(getpass.getuser())

pdfFile = canvas.Canvas('./python.pdf')
pdfFile.saveState()

pdfFile.setAuthor(getpass.getuser())
pdfFile.setTitle('PDF生成')
pdfFile.setSubject('サンプル')

# A4
#pdfFile.setPageSize((18.2 * cm, 25.7 * cm))
# B5
pdfFile.setPageSize((18.2*cm, 25.7*cm))

pdfFile.setFillColorRGB(0, 0, 0)

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
pdfFile.setFont('HeiseiKakuGo-W5', 12)

#pdfFile.drawString(5*cm, 25*cm, 'あいうえおー')
pdfFile.drawString(13.5 * cm, 25.7*cm - 2.7 * cm, "3")

pdfFile.restoreState()
pdfFile.save()
