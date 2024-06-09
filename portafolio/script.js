let imagenes = document.querySelectorAll('.barrido');

function imagenVisible(imagen)
{
    let borde = imagen.getBoundingClientRect();
    if (borde.top < window.innerHeight && borde.bottom > 0)
    {
        imagen.classList.add('visible');
    }
    else
    {
        imagen.classList.remove('visible');
    }
}
function estaVisible()
{
    imagenes.forEach(imagenVisible);
}

window.addEventListener('scroll', estaVisible);
window.addEventListener('resize', estaVisible);