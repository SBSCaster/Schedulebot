import discord
from discord.ext import commands
import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os


class schedule_logic(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.days_from_text = []

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
        cvt = svg2rlg(svgname)
        renderPM.drawToFile(cvt, f'{info[0]}.png', fmt='PNG')
        
        

    
    @commands.command()
    async def postschedule(self, ctx):
        with open('itachi.txt', 'r') as file:
            for line in file.readlines():
                if ';' in line.splitlines()[0]:
                    self.days_from_text.append(line.strip('\n'))

        for day in self.days_from_text:
            schedule_logic.convert_text_to_svg(day=day)
            info = day.split(';')
            await ctx.send(file=discord.File(f'{info[0]}.png'))
            os.remove(f'{info[0]}.svg')
            os.remove(f'{info[0]}.png')




def setup(client):
    client.add_cog(schedule_logic(client))