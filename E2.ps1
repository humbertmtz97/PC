Function menu {
    Clear-Host
    Write-Host "Starting Menu..."
    Write-Host "1. Si quieres explorar los módulos importados en tu sesión actual"
    Write-Host "2. Para ver los comandos importados por cada módulo puedes usar"
    Write-Host "3. Para ver el perfil de nuestra red actual podemos usar el comando"
    Write-Host "4. Obtiene los procesos que se ejecutan en el equipo local."
    Write-Host "5. Obtiene los servicios del equipo"
    Write-Host "6. Exit"
}
 
menu
 
while(($inp = Read-Host -Prompt "Selecciona una opcion") -ne "6"){
 
switch($inp){
        1 {
            Clear-Host
Get-Command

            pause;
            break
        }
        2 {
            Clear-Host
Get-Verb

            pause; 
            break
        }
        3 {
            Clear-Host
Get-NetConnectionProfile 
 
            pause;
            break
            }
        4 {
            Clear-Host
Get-Process   
            pause;
            break
            }
        5 {
            Clear-Host
Get-Service
            pause;
            break
            }

        6 {"Exit"; break}
        default {Write-Host -ForegroundColor red -BackgroundColor white "Invalid option. Please select another option";pause}
        
    }
 
menu
}