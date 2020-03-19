import subprocess
import tempfile
import os
current_path = os.getcwd()
def yomiage(text):
    dict_path = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
    voice_path = current_path + '/voice/mei_nomal.htsvoice'
    talk_speed = '1.0'
    out_wav_name = current_path + '/tmp/yomiage_tmp.wav'
    # make command
    generate_talk_wav_command = f'open_jtalk -x {dict_path} -m {voice_path} -r {talk_speed} -ow {out_wav_name}'
    result = subprocess.run([generate_talk_wav_command], stdin=subprocess.PIPE)
    result.stdin.write(text.encode())
    result.stdin.close()
    yomiage_command = f'aplay -q {out_wav_name}'
    subprocess.run([yomiage_command])
    return True
    



