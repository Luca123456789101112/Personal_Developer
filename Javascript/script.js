dineroR = prompt("Cuanto dinero tiene roberto")
dineroP = prompt("Cuanto dinero tiene pedro")
dineroC = prompt("Cuanto dinero tiene cofla")

//lado cofla

vueltoR = 0
vueltoP = 0
vueltoC = 0

//><
if (dineroC <= 1 && dineroC >=0.6){
	alert("cofla comprate el palito de agua")
	vueltoC = dineroC - 1
	alert(vueltoC)
}
else if (dineroC <= 1.6 && dineroC >=1){
	alert("cofla comprate el helado de crema")
	vueltoC = dineroC - 1.6
	alert(vueltoC)
}
else if (dineroC <= 1.7 && dineroC >=1.6){
	alert("cofla comprate el helado marca heladix")
	vueltoC = dineroC - 1.7
	alert(vueltoC)
}
else if (dineroC <= 1.8 && dineroC >=1.7){
	alert("cofla comprate el helado marca helardovich")
	vueltoC = dineroC - 1.8
	alert(vueltoC)
}
else if (dineroC >= 2.9){
	alert("cofla comprate el helado marca helardo")
	vueltoC = dineroC - 1.8
	alert(vueltoC)
}
else{
	alert("andate de aca pobre, no te alcanza para nada")
}
//parte pedro

if (dineroP <= 1 && dineroP >=0.6){
	alert("pedro comprate el palito de agua")
	alert(dineroP-1)
}
else if (dineroP <= 1.6 && dineroP >= 1){
	alert("pedro comprate el helado de crema")
	alert(dineroP-1.6)
}
else if (dineroP <= 1.7 && dineroP >=1.6){
	alert("pedro comprate el helado marca heladix")
	alert(dineroP-1.7)
}
else if (dineroP <= 1.8 && dineroP >=1.7){
	alert("pedro comprate el helado marca helardovich")
	alert(dineroP-1.8)
}
else if (dineroP >= 2.9){
	alert("pedro comprate el helado marca helardo")
	alert(dineroP-2.9)
}
else{
	alert("andate de aca pobre, no te alcanza para nada")
}

// parte roberto

if (dineroR <= 1 && dineroR >=0.6){
	alert("roberto  comprate el palito de agua")
	alert(dineroR-1)
}
else if (dineroR <= 1.6 && dineroR >=1){
	alert("roberto  comprate el helado de crema")
	alert(dineroR-1.6)
}
else if (dineroR <= 1.7 && dineroR >=1.6){
	alert("roberto  comprate el helado marca heladix")
	alert(dineroR-1.7)
}
else if (dineroR <= 1.8 && dineroR >=1.7){
	alert("roberto  comprate el helado marca helardovich")
	alert(dineroR-1.8)
}
else if (dineroR >= 2.9){
	alert("roberto comprate el helado marca helardo")
	alert(dineroR-2.9)
}
else{
	alert("andate de aca pobre, no te alcanza para nada")
}
