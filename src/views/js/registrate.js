function formValidation() {
    //debugger;
    var nombreUsuario = document.getElementById("nombreUsuario").value.trim();
    var mailDeUsuario = document.getElementById("mailDeUsuario").value.trim();
    var clave = document.getElementById("clave").value.trim();
    var repeticionDeClave = document.getElementById("repeticionDeClave").value.trim();

    errores=""
    if (nombreUsuario=="") {
        errores=errores+"Debe proporcionar un nombre de usuario. "
    } else if (nombreUsuario.length<6) {
        errores=errores+"Nombre de usuario demasiado corto, deben ser al menos 6 caracteres. "
    } else if (nombreUsuario.length>20) {
        errores=errores+"Nombre de usuario demasiado largo, deben ser como máximo 20 caracteres. "
    }


    if (clave=="") {
        errores=errores+"Debe proporcionar una clave. "
    } else if (clave.length<8) {
        errores=errores+"Clave demasiado corta, deben ser al menos 8 caracteres. "
    } else if (clave.length>=60) {
        errores=errores+"Clave demasiado larga,  deben ser como máximo 60 caracteres. "
    } else if (clave!=repeticionDeClave) {
        errores=errores+"Las claves no coinciden. "
    }

    if (mailDeUsuario=="") {
        errores=errores+"Debe proporcionar un email. "
    } else if (mailDeUsuario.indexOf("@")==-1) {
        errores="Debe proporcionar una dirección de mail válida. "
    }

    if (errores=="") {
        // llamada al backend, con los datos ya validados

        // SI el backnd responde OK
            document.getElementById("mensajeDeError").style.display="none";
            document.getElementById("botonRegistro").style.display="none";
            document.getElementById("mensajeExitoso").style.display="block";

        // SINO (si el backend no pudo guardar el suario)

            //document.getElementById("mensajeDeError").textContent= Lo que sea q haya venido como mensaje de error del back;
            //document.getElementById("mensajeDeError").style.display="block";

        // FIN
    } else {
        document.getElementById("mensajeDeError").textContent=errores;
        document.getElementById("mensajeDeError").style.display="block";
        console.log("Hay errores: "+errores)
    }
    console.log(nombreUsuario);
    return false;

} 

