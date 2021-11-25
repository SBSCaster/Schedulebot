'''import svgwrite

days = ['Monday', 'Tuesday', 'Wendseday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_from_text = []

with open('itachi.txt', 'r') as file:
    for line in file.readlines():
        if ';' in line.splitlines()[0]:
            days_from_text.append(line.strip('\n'))


svg_doc = svgwrite.Drawing(filename='test.svg',
                        size=('800px', '600px'))

svg_doc.add(svg_doc.rect(insert = (0, 150),
                                   size = ("600px", "450px"),
                                   stroke_width = "1",
                                   stroke = "black",
                                   fill = "rgb(50,50,0)"))

svg_doc.add(svg_doc.rect(insert=(0,0),
                                size=('600px', '150px'),
                                fill= 'rgb(100,0,0)'))


svg_doc.add(svg_doc.text("Date/Time Could Go Here",
                                   insert = (180, 60)))

svg_doc.add(svg_doc.text("Descripton/Teammembers/etc could go here",
                                    insert=(180, 200)))



print(svg_doc.tostring())

svg_doc.save()
'''
"""import svgwrite




def convert_text_to_svg(day):
    info = day.split(';')
    svgname = f'{info[0]}.svg'
    svg_doc = svgwrite.Drawing(filename=svgname,
                        size=('800px', '600px'))
    svg_doc.add(svg_doc.rect(insert = (0, 150),
                                   size = ("600px", "450px"),
                                   stroke_width = "1",
                                   stroke = "black",
                                   fill = "rgb(50,50,0)"))

    svg_doc.add(svg_doc.rect(insert=(0,0),
                                size=('600px', '150px'),
                                fill= 'rgb(100,0,0)'))
    svg_doc.add(svg_doc.text(f'{info[0]}: {info[1]}',
                                   insert = (180, 60)))

    svg_doc.add(svg_doc.text(info[2],
                                    insert=(180, 200)))
    svg_doc.save()


days = ['Monday', 'Tuesday', 'Wendseday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_from_text = []

with open('itachi.txt', 'r') as file:
    for line in file.readlines():
        if ';' in line.splitlines()[0]:
            days_from_text.append(line.strip('\n'))

for day in days_from_text:
    convert_text_to_svg(day=day)"""



    

