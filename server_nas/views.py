# from subprocess import CalledProcessError
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_unix_user(request):
    nim = request.POST.get('nim')
    id = request.POST.get('id')
    print(id)
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

