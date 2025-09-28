from django.shortcuts import render

# CRUD Views


class DocumentListView(ListView):
    model = Document
    template_name = 'documents/document_list.html'
    context_object_name = 'documents'


class DocumentCreateView(CreateView):
    model = Document
    fields = ['title', 'file'] # Fields to show in the form
    template_name = 'documents/document_form.html'
    success_url = reverse_lazy('document_list') # Redirect after successful upload
    
    
class DocumentUpdateView(UpdateView):
    model = Document
    fields = ['title'] # Only allow editing the title
    template_name = 'documents/document_form.html'
    # success_url is handled by get_absolute_url in the model
    
    
class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'documents/document_confirm_delete.html'
    success_url = reverse_lazy('document_list') # Redirect after successful deletion