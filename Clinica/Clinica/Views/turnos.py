from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist


import io
import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from Datos.models import Usuario, Persona, Turno


def generarPDF(post, elemento):
    response = HttpResponse(content_type ='application/pdf')
    pdf_name = "menu.pdf"
    response['Content-Disposition'] = f'attachment; filename="Comprobante de consulta.pdf'

    buff = io.BytesIO()

    doc = SimpleDocTemplate(buff, pagesize=A4,
                            rightMargin=62, leftMargin=62,
                            topMargin=62, bottomMargin=7)
    Story = []
    logo = "../Clinica/Static/images/logo.png"
    magName = 'Clinica "Lorem Ipsum"'


    styles = getSampleStyleSheet()
    ptext = '<font size="12"><b>----------------------------------------------COMPROBANTE----------------------------------------------</b></font>'

    persona = elemento.fk_persona_dni

    im = Image(logo, 2 * inch, 1 * inch)
    Story.append(im)
    styles = getSampleStyleSheet()

    Story.append(Spacer(1, 16))

    Story.append(Spacer(1, 12))
    ptext = '<font size="12"><b>-------------------------------------------------PACIENTE-------------------------------------------------</b></font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12"><b>El siguiente archivo sirve como comprobante de la solicitud del turno, este debera ser entregado en la secretaria el dia que se presente en la clinica donde ademas se le pedira documentacion respaldatoria.</b></font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = f'<font size="12"><b>Fecha de creacion del informe:</b> {datetime.date.today().strftime("%d/%m/%Y")}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Paciente:</b> {persona.nombre}, {persona.apellido}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>DNI del paciente:</b> {persona.dni}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Fecha de nacimeinto:</b> {persona.nacimiento.strftime("%d/%m/%Y")}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Telefono del paciente:</b> {persona.telefono}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Domicilio del paciente:</b> {persona.domicilio}, {persona.localidad}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = '<font size="12"><b>-------------------------------------DATOS DE LA CONSULTA-------------------------------------</b></font>'

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12"><b>Medico con el que se atendera:</b> {post["medico"]}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Forma de pago:</b> {post["FormaPago"]} ({post["Tipo"]})</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Fecha de la consulta:</b> {post["Fecha"]}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))


    doc.build(Story)

    response.write(buff.getvalue())
    buff.close()

    return response
"""
    Story.append(PageBreak())

    im = Image(logo, 2 * inch, 1 * inch)
    Story.append(im)

    Story.append(Spacer(1, 16))

    ptext = '<font size="12"><b>------------------------------------------ESPACIO DE NOTAS------------------------------------------</b></font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 32))

    for x in range(25):
        ptext = '<font size="12">____________________________________________________________________</font>'
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
"""



def landing(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        nombre = request.session.get('actual')
        elemento = Usuario.objects.get(user=nombre)
        """try:
            historial = Salud.objects.get(fk_persona_dni=elemento.fk_persona_dni)
        except ObjectDoesNotExist:
            historial = None"""

        """print(historial)"""
        # print(elemento)
        """contexto = {"usuario": elemento, "persona": elemento.fk_persona_dni, "historial": historial}"""

        if request.POST:
            post = request.POST

            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(post.keys())

            if post["discriminador"] == "confirmar":
                nuevoTurno = Turno()
                nuevoTurno.fk_persona_dni = elemento.fk_persona_dni
                nuevoTurno.especialista = post["medico"]
                nuevoTurno.pago = post["FormaPago"]
                nuevoTurno.nombrePago = post["Tipo"]
                nuevoTurno.fecha = post["Fecha"]

                nuevoTurno.save()
                return generarPDF(post, elemento)

            elif post["discriminador"] == "comprobante":
                # buffer = generarPDF(None, None)
                return generarPDF(post)

        # return redirect("menu")
        print(request.session.get('actual'))
        return render(request, "turnos.html")