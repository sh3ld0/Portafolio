let images = document.querySelectorAll('.fade-in');

function toggleVisibility(image)
{
    let rect = image.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0)
    {
        image.classList.add('visible');
    }
    else
    {
        image.classList.remove('visible');
    }
}
function checkVisibility()
{
    images.forEach(toggleVisibility);
}

window.addEventListener('scroll', checkVisibility);


window.addEventListener('resize', checkVisibility);