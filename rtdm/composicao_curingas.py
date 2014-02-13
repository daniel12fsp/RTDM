
composicao_curingas = {

	"asterisco,asterisco ": "asterisco",
	"asterisco,mais ": "asterisco",
	"asterisco,interrogacao ": "asterisco",
	"asterisco,ponto ": "asterisco",
	"mais,mais ": "mais",
	"mais,ponto ": "mais",
	"mais,interrogacao ": "asterisco",
	"ponto,ponto ": "ponto",
	"ponto,interrogacao ": "interrogacao",
	"interrogacao,interrogacao ": "interrogacao"
}

def get_curinga(n1, n2):
	if(type(n1) is str):
		return composicao_curingas[n1+","+n2]
	else:
		return composicao_curingas[n1.name+","+n2.name]
	



