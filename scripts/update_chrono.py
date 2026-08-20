"""Sincroniza el reloj CHRONO de assets/panels.svg con la hora de Argentina (UTC-3).

Reescribe los angulos iniciales de las agujas (que luego siguen avanzando en
tiempo real via SMIL) y la hora/fecha digital. Pensado para correr desde un
GitHub Action cada 15 minutos.
"""
import io
import re
from datetime import datetime, timezone, timedelta

SVG = 'assets/panels.svg'
ART = timezone(timedelta(hours=-3))  # Argentina no tiene horario de verano
DOW = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

now = datetime.now(ART)
sec = now.second
minute = now.minute + sec / 60
hour = (now.hour % 12) + minute / 60

sec_a = sec * 6.0
min_a = minute * 6.0
hour_a = hour * 30.0

s = io.open(SVG, encoding='utf-8').read()

def set_hand(src, dur, angle):
    pat = r'from="[-\d.]+ 610 130" to="[-\d.]+ 610 130" dur="%s"' % dur
    new = 'from="%.1f 610 130" to="%.1f 610 130" dur="%s"' % (angle, angle + 360, dur)
    out, n = re.subn(pat, new, src)
    assert n == 1, 'no se encontro la aguja dur=%s' % dur
    return out

s = set_hand(s, '43200s', hour_a)
s = set_hand(s, '3600s', min_a)
s = set_hand(s, '60s', sec_a)

digital = ('<text x="610" y="222" text-anchor="middle" font-size="16" fill="#e6edf3">'
           '%02d<tspan fill="#58f0a8">:</tspan>%02d</text>' % (now.hour, now.minute))
s, n = re.subn(r'<text x="610" y="222" text-anchor="middle" font-size="16" fill="#e6edf3">.*?</text>',
               digital, s)
assert n == 1, 'no se encontro la hora digital'

sub = ('<text x="610" y="248" text-anchor="middle" font-size="12" fill="#5b6a77">'
       '%s %04d.%02d.%02d // UTC-3</text>' % (DOW[now.weekday()], now.year, now.month, now.day))
s, n = re.subn(r'<text x="610" y="248" text-anchor="middle" font-size="12" fill="#5b6a77">.*?</text>',
               sub, s)
assert n == 1, 'no se encontro la linea de fecha'

io.open(SVG, 'w', encoding='utf-8', newline='\n').write(s)
print('chrono -> %s' % now.strftime('%Y-%m-%d %H:%M:%S ART'))
