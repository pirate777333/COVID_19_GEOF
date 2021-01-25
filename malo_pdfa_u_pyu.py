from fpdf import FPDF

pdf=FPDF('P','mm','A4')
pdf.add_page()
pdf.set_font("Arial","B",24)
pdf.set_text_color(202,49,49)
#pdf.cell(40,10,'Hello')
pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/for_prax/4305157.jpg",0,0,210,100)
pdf.text(100,10,'COVID-19 Analytics Report')

pdf.set_font("Arial","B",16)
pdf.set_text_color(0,0,0)

pdf.text(90,130,'Made by:')
pdf.text(84,140,'Duje Petkovic')

pdf.set_font("Arial","I",12)

pdf.text(97,160,'Date:')
pdf.text(91,170,'21/12/2020')

pdf.text(83,190,'Sveuciliste u Zagrebu')
pdf.text(86,200,'Geodetski fakultet')
pdf.text(78,210,'Usmjerenje: Geoinformatika')

pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/for_prax/19007.jpg",0,220,210,77)

pdf.add_page()

pdf.set_font("Arial","B",16)
pdf.text(20,20,'Usporedba sirenja COVID-19 virusa u:')
pdf.set_font("Arial","I",12)
pdf.text(20,30,'Hrvatskoj, Sloveniji i Srbiji')

pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/gpadas_W.png",5,40,190,100) # SVIJET
pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/gpadas_EU.png",5,170,190,100) # EUROPA

pdf.add_page()

pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_totalnew.png",5,20,190,110) # SVIJET
pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_dailynew.png",5,150,190,110) # EUROPA

pdf.add_page()

pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_totaldeath.png",5,20,190,110) # SVIJET
pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_dailydeath.png",5,150,190,110) # EUROPA

pdf.add_page()

pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_bar_new.png",5,20,95,100) # SVIJET
pdf.image("C:/Users/Josko/Desktop/GeoViz/esej/css_bar_death.png",105,20,95,100) # EUROPA

pdf.set_font("Arial","B",14)
pdf.text(20,140,'Svi graficki prikazi odnose se na period:')
pdf.text(20,145,'01.10.2020. - 21.12.2020.')

pdf.output('COVID19_Report.pdf','F')
