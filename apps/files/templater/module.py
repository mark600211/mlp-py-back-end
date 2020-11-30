from ..grpc.client.module import getAct
from docxtpl import DocxTemplate


def getAct(id: str):
    act = getAct(id)

    return act


def createDocFromTemplate(id: str):
    doc = DocxTemplate("template.docx")

    act = getAct(id)

    context = {'customer': act.customer.label, 'generalCustomer':
               act.generalCustomer.label, 'typeOfSample': act.typeOfSample.label, 'applications': act.applications}

    doc.render(context)
    doc.save("generated_doc.docx")

