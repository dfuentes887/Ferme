from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

def render_to_pdf(template_src,context_dict={}):
    template = get_template (template_src)
    
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf' )
    filename="report.pdf"
   
    pisaStatus = pisa.CreatePDF(
    html, dest= response
    )
    result = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type = 'application/pdf')
    
    return None
