import os

d = 'F:/BaiduNetdiskDownload/SoftwareProject/youdaonote-pull/youdaonote'
files = []
for r, dirs, files_list in os.walk(d):
    for f in files_list:
        files.append(os.path.join(r, f))

def magic(path):
    try:
        with open(path, 'rb') as f:
            b = f.read(16)
            return b.hex()
    except Exception as e:
        return str(e)

audio_files = [f for f in files if f.endswith('.audio')]
scan_files = [f for f in files if f.endswith('.scan')]
no_ext = [f for f in files if '.' not in os.path.basename(f) and os.path.isfile(f)]

print('Audio 1:', audio_files[0] if audio_files else 'None')
if audio_files:
    print('  Magic:', magic(audio_files[0]))

print('Scan 1:', scan_files[0] if scan_files else 'None')
if scan_files:
    print('  Magic:', magic(scan_files[0]))

print('No ext 1:', no_ext[0] if no_ext else 'None')
if no_ext:
    print('  Magic:', magic(no_ext[0]))
