# from subprocess import CalledProcessError
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_unix_user(request):
    nim = request.POST.get('nim')
    print(nim)
    try:
        subprocess.check_call(
            'useradd -p $(openssl passwd -1 ' + str(nim) + ') -m -s /bin/bash -g hosting-users '
            + str(nim), #+ ' && quotatool -u ' + self.userId + ' -bq 450M -l 500M /home',
            shell=True)
    except subprocess.CalledProcessError:
        return JsonResponse({'status': 'error', 'message': 'Error adding Unix user'})
    else:
        return JsonResponse({'status': 'success', 'message': 'Unix user added'})


@csrf_exempt
def izin_user(request):
    if request.method == 'POST':
        data = request.POST  # Use request.POST for application/x-www-form-urlencoded data
        # Alternatively, use request.body for application/json data
        container_id = data.get('container_id')
        nim_user = data.get('nim_user')
        kategori_kontainer = data.get('kategori_kontainer')

        # Validate the data (add your validation logic here)
        if not container_id or not nim_user or not kategori_kontainer:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # Prepare the chown command
        command = f'chown {nim_user}:hosting-users -R /home/{nim_user}/{kategori_kontainer}'

        try:
            # Execute the chown command using subprocess
            subprocess.run(command, shell=True, check=True)
            return JsonResponse({'status': 'success', 'message': 'Command executed successfully'})
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': f'Error executing command: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
