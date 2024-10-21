from django.shortcuts import render

# Create your views here.

def index(request):
    categorias = ['Electrónica', 'Ropa', 'Juguetes']
    return render(request, 'app/index.html', {'categorias': categorias})

# Vista para los productos
def productos(request, categoria):
    productos = {
        'Electrónica': ['Smartphone', 'Laptop', 'Tablet'],
        'Ropa': ['Camisa', 'Pantalones', 'Zapatos'],
        'Juguetes': ['Pelota', 'Figura', 'Peluche']
    }
    return render(request, 'app/productos.html', {'categoria': categoria, 'productos': productos[categoria]})