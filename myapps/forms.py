from django import forms  
from .models import Devis,DevisDemande

class DevisForm(forms.ModelForm):
                
	class Meta:  
         model = Devis 
         fields = "__all__"  
         
class DevisDemandeForm(forms.ModelForm):
        class Meta:  
         model = DevisDemande 
         fields = "__all__"  
        