from django.http import HttpResponse, FileResponse
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





from Datos.models import Usuario, Persona, Salud


def generarPDF(persona, salud):
    response = HttpResponse(content_type ='application/pdf')
    pdf_name = "menu.pdf"
    response['Content-Disposition'] = f'attachment; filename="Ficha medica de {persona.apellido}, {persona.nombre}.pdf'

    buff = io.BytesIO()

    doc = SimpleDocTemplate(buff, pagesize=A4,
                            rightMargin=62, leftMargin=62,
                            topMargin=62, bottomMargin=7)
    Story = []
    logo = "../Clinica/Static/images/logo.png"
    magName = 'Clinica "Lorem Ipsum"'

    im = Image(logo, 4 * inch, 2 * inch)
    Story.append(im)
    styles = getSampleStyleSheet()

    Story.append(Spacer(1, 64))
    title_style = styles['Heading1']
    title_style.alignment = 1
    ptext = '<font size="42">Clinica "Lorem Ipsum"</font>'
    Story.append(Paragraph(ptext, title_style))
    Story.append(Spacer(1, 32))
    ptext = '<font size="30">Ficha medica</font>'
    Story.append(Paragraph(ptext, title_style))
    Story.append(Spacer(1, 32))

    Story.append(PageBreak())

    im = Image(logo, 2 * inch, 1 * inch)
    Story.append(im)
    styles = getSampleStyleSheet()

    Story.append(Spacer(1, 16))

    Story.append(Spacer(1, 12))
    ptext = '<font size="12"><b>-----------------------------------------DATOS PERSONALES-----------------------------------------</b></font>'
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
    ptext = '<font size="12"><b>--------------------------------------------DATOS MEDICOS--------------------------------------------</b></font>'

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = f'<font size="12"><b>Grupo sanguineo:</b> {""if (salud is None) else salud.grupoSanguineo}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Fumador:</b> {""if (salud is None) else "Si" if (salud.fuma == "fsi") else "Socialmente" if (salud.fuma == "fsoc") else "No"}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Bebedor:</b> {""if (salud is None) else "Si" if (salud.bebe == "bsi") else "Socialmente" if (salud.bebe == "bsoc") else "No"}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Alergias:</b> {""if (salud is None) else salud.alergias}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Medicamentos que consume:</b> {""if (salud is None) else salud.medicamentos}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Enfermedades cronicas:</b> {""if (salud is None) else salud.enfcronica}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))
    ptext = f'<font size="12"><b>Antecendentes quirurgicos:</b> {""if (salud is None) else salud.antquirurgicos}</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))

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

    doc.build(Story)

    response.write(buff.getvalue())
    buff.close()

    return response


def landing(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        nombre = request.session.get('actual')
        elemento = Usuario.objects.get(user=nombre)
        try:
            historial = Salud.objects.get(fk_persona_dni=elemento.fk_persona_dni)
        except ObjectDoesNotExist:
            historial = None

        print(historial)
        # print(elemento)
        contexto = {"usuario": elemento, "persona": elemento.fk_persona_dni, "historial": historial}

        if request.POST:
            post = request.POST

            if post["discriminador"] == "personal":
                persona = elemento.fk_persona_dni
                persona.nombre = post["Nombre"]
                persona.apellido = post["Apellido"]
                persona.nacimiento = post["Nacimiento"]
                persona.telefono = post["Telefono"]
                persona.localidad = post["Localidad"]
                persona.domicilio = post["Direccion"]

                persona.save()

                elemento.email = post["Correo"]

                elemento.save()

            elif post["discriminador"] == "salud":
                if historial is None:
                    historial = Salud()

                historial.fk_persona_dni = elemento.fk_persona_dni
                historial.grupoSanguineo = post["sangre"]
                historial.fuma = post["fuma"]
                historial.bebe = post["bebe"]
                historial.alergias = post["Alergias"]
                historial.medicamentos = post["Medicamentos"]
                historial.enfcronica = post["EnfermedadesCronicas"]
                historial.antquirurgicos = post["Cirugias"]

                historial.save()

            elif post["discriminador"] == "ficha":
                #buffer = generarPDF(None, None)
                return generarPDF(elemento.fk_persona_dni, historial)

        #



        html = loader.get_template("covid.html")
        # return redirect("menu")
        #print(request.session.get('actual'))
        return render(request, "perfil.html", contexto)