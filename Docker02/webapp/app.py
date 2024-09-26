import web
import os
import uuid

urls = (
    '/', 'Index',
    '/upload', 'Upload'
)

upload_dir = 'static/pdf'

if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

class Upload:
    def POST(self):
        x = web.input(archivo_pdf={})
        
        if 'archivo_pdf' in x:
            original_filename = x['archivo_pdf'].filename

            if not original_filename.endswith('.pdf'):
                return "El archivo debe ser un PDF."
            
            unique_filename = f"{uuid.uuid4()}.pdf"
            
            file_path = os.path.join(upload_dir, unique_filename)
            with open(file_path, 'wb') as saved_file:
                saved_file.write(x['archivo_pdf'].file.read())
                
            return render.upload() 
        else:
            return "No se ha subido ningún archivo."

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
