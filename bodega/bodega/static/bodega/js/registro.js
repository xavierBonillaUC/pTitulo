


$(function registrar() {
    $('#btnCrear').on('click', function () {
        var rol, nombre, contrasena, contrasenaVe;
        rol = $("#nrol").val();
        nombre = $("#nombre").val();
        contrasena = $("#contrasena").val();
        contrasenaVe = $("#contrasenaVe").val();
        

         
        if(nombre == " "){
            alert("Ingrese un nombre por favor");
            return false;
    
        }
        else if(contraseña == ""){
            alert("El campo Télefono está vacio");
                
        } 
        
        
        
        else if(contrasena== ""){
            alert("El campo está vacio");
            
        } 
        else if(contrasenaVe== ""){
            alert("El campo está vacio");
            
        } 

        
  

    })
    
})



