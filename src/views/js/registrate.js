function formValidation() {
    //debugger;
    var nombreUsuario = document.getElementById("nombreUsuario").value.trim();
    var mailDeUsuario = document.getElementById("mailDeUsuario").value.trim();
    var clave = document.getElementById("clave").value.trim();
    var repeticionDeClave = document.getElementById("repeticionDeClave").value.trim();

    errores = ""
    if (nombreUsuario == "") {
        errores = errores + "Debe proporcionar un nombre de usuario. "
    } else if (nombreUsuario.length < 2) {
        errores = errores + "Nombre de usuario demasiado corto, deben ser al menos 2 caracteres. "
    } else if (nombreUsuario.length > 20) {
        errores = errores + "Nombre de usuario demasiado largo, deben ser como máximo 20 caracteres. "
    }

    if (clave == "") {
        errores = errores + "Debe proporcionar una clave. "
    } else if (clave.length < 8) {
        errores = errores + "Clave demasiado corta, deben ser al menos 8 caracteres. "
    } else if (clave.length >= 60) {
        errores = errores + "Clave demasiado larga,  deben ser como máximo 60 caracteres. "
    } else if (clave != repeticionDeClave) {
        errores = errores + "Las claves no coinciden. "
    }

    if (mailDeUsuario == "") {
        errores = errores + "Debe proporcionar un email. "
    } else if (mailDeUsuario.indexOf("@") == -1) {
        errores = "Debe proporcionar una dirección de mail válida. "
    }

    if (errores == "") {
        // llamada al backend, con los datos ya validados
        $.ajax({
            type: "POST",
            url: "http://bsp-cuidapets.xh.ar/api/user/register",
            data: JSON.stringify({
                username: nombreUsuario, password: clave, email: mailDeUsuario
            }),
            contentType: "application/json; charset=utf-8",
            success: function (result) {
                //      debugger;
                if (result.status == "ok") {
                    // SI el backnd responde OK
                    document.getElementById("mensajeDeError").style.display = "none";
                    document.getElementById("botonRegistro").style.display = "none";
                    document.getElementById("mensajeExitoso").style.display = "block";
                } else {
                    // SINO (si el backend no pudo guardar el suario)
                    document.getElementById("mensajeDeError").textContent = result.message;
                    document.getElementById("mensajeDeError").style.display = "block";
                }
                // FIN
            },
            failure: function (errMsg) { console.log(errMsg); }
        });
    } else {
        document.getElementById("mensajeDeError").textContent = errores;
        document.getElementById("mensajeDeError").style.display = "block";
        console.log("Hay errores: " + errores)
    }
    console.log(nombreUsuario);
    return false;
}


function cerrarSesion(){
    localStorage.removeItem('email');
    localStorage.removeItem('sessionToken');

    document.getElementById("menuRegistrate").style.display = "block";
    document.getElementById("menuIniciarSesion").style.display = "block";
    document.getElementById("menuCerrarSesion").style.display = "none";
    document.getElementById("iniciarSesionError").style.display = "none";    
}

function login(){
    var loginUserName = document.getElementById("loginUserName").value.trim();
    var loginPassword = document.getElementById("loginPassword").value.trim();

    errores = ""
    if (loginUserName == "") {
        errores = errores + "Debe proporcionar un nombre de usuario. "
    }

    if (loginPassword == "") {
        errores = errores + "Debe proporcionar una clave. "
    }

    if (errores == "") {

        document.getElementById("iniciarSesionError").style.display = "none";
        document.getElementById("iniciarSesionSpinner").style.display = "block";
        // llamada al backend, con los datos ya validados
        $.ajax({
            type: "POST",
            url: "http://bsp-cuidapets.xh.ar/api/login",
            data: JSON.stringify({
                username: loginUserName, password: loginPassword
            }),
            contentType: "application/json; charset=utf-8",
            success: function (result) {
                //debugger;
                if (result.status == "ok") {
                    console.log(result);
                    $("#IniciarSesionModal").modal("toggle");
                    localStorage.setItem('sessionToken',result.additionalData.sessionToken);
                    localStorage.setItem('email',result.additionalData.email);

                    document.getElementById("menuRegistrate").style.display = "none";
                    document.getElementById("menuIniciarSesion").style.display = "none";
                    document.getElementById("menuCerrarSesion").style.display = "block";
                    document.getElementById("menuCerrarSesionLink").textContent = "Cerrar sesion "+localStorage.getItem('email');

                    // SI el backnd responde OK
                    //document.getElementById("mensajeDeError").style.display = "none";
                    //document.getElementById("botonRegistro").style.display = "none";
                    //document.getElementById("mensajeExitoso").style.display = "block";
                } else {
                    console.log(result);
                    document.getElementById("iniciarSesionError").textContent=result.message;
                    document.getElementById("iniciarSesionError").style.display = "block";
                    // SINO (si el backend no pudo guardar el suario)
                    //document.getElementById("mensajeDeError").textContent = result.message;
                    //document.getElementById("mensajeDeError").style.display = "block";
                }
                document.getElementById("iniciarSesionSpinner").style.display = "none";
                // FIN
            },
            error: function (errMsg) { 
                //debugger;
                console.log(errMsg); 
                document.getElementById("iniciarSesionSpinner").style.display = "none";
                document.getElementById("iniciarSesionError").textContent=errMsg.statusText;
                document.getElementById("iniciarSesionError").style.display = "block";
        }
        });
    } else {
        //document.getElementById("mensajeDeError").textContent = errores;
        //document.getElementById("mensajeDeError").style.display = "block";
        document.getElementById("iniciarSesionError").style.display = "block";
        console.log("Hay errores: " + errores)
    }
    console.log(nombreUsuario);
    return false;

}



