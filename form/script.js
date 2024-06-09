function procesar()
{
    let primerNombre = document.getElementById('primerNombre').value;
    let segundoNombre = document.getElementById('segundoNombre').value;
    let primerApellido = document.getElementById('primerApellido').value;
    let segundoApellido = document.getElementById('segundoApellido').value;
    let dni = document.getElementById('dni').value;
    let fechaNacimiento = document.getElementById('fechaNacimiento').value;
    let Valido = true;
    if(primerNombre === '')
        {
            campo_Invalido('primerNombre');
            Valido=false;
        }
    else
        {
            campo_Valido('primerNombre');
        }
    if(segundoNombre === '')
        {
            campo_Invalido('segundoNombre');
            Valido=false;
        }
    else
        {
            campo_Valido('segundoNombre');
        }
    if(primerApellido === '')
        {
            campo_Invalido('primerApellido');
            Valido=false;
        }
    else
        {
            campo_Valido('primerApellido');
        }
    if(segundoApellido === '')
        {
            campo_Invalido('segundoApellido');
            Valido=false;
        }
    else
        {
            campo_Valido('segundoApellido');
        }
    if(dni === '')
        {
            campo_Invalido('dni');
            Valido=false;
        }
    else
        {
            campo_Valido('dni');
        }
    if(fechaNacimiento === '')
        {
            campo_Invalido('fechaNacimiento');
            Valido=false;
        }
    else
        {
            campo_Valido('fechaNacimiento');
        }
    if(!Valido)
        {
            return;
        }
    let nombreCompleto = `${primerNombre} ${segundoNombre} ${primerApellido} ${segundoApellido}`;
    let ultimoDigitoDni = dni.charAt(dni.length - 1);
    let fechaNacimientoDate = new Date(fechaNacimiento);
    let edad = new Date().getFullYear() - fechaNacimientoDate.getFullYear();
    let mes = new Date().getMonth() - fechaNacimientoDate.getMonth();
    console.log("despues de if")
    if (mes < 0 || (mes === 0 && new Date().getDate() < fechaNacimientoDate.getDate()))
    {
        edad--;
    }
    document.getElementById('nombreCompleto').value = nombreCompleto;
    document.getElementById('ultimoDigitoDni').value = ultimoDigitoDni;
    document.getElementById('edad').value = edad;
}
function campo_Invalido(id)
{
    document.getElementById(id).classList.add('is-invalid');
}
function campo_Valido(id)
{
    document.getElementById(id).classList.remove('is-invalid');
}