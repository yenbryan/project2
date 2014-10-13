from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from discussion.forms import CommentForm, DiscussionForm
from discussion.models import Discussion, Category, Comment


@login_required()
def post_discussion(request):

    data = {}
    return render(request, 'discussion/post_discussion.html', data)

@login_required()
def discussions(request):
    categories = Category.objects.all()
    discussions = Discussion.objects.all()
    data = {'discussions': discussions,
            'discussionactive': 'active',
            'categories': categories}
    return render(request, 'discussion/discussions.html', data)


@login_required()
def view_discussion(request, discussion_id):
    # Might need a try/except in case there is a bad discussion_id passed in
    discussion = Discussion.objects.get(id=discussion_id)
    comments = Comment.objects.filter(discussion=discussion)
    comment_form = CommentForm()
    data = {'discussionactive': 'active',
            'discussion': discussion,
            'comments': comments,
            'comment_form': comment_form}
    return render(request, 'discussion/view_discussion.html', data)

@login_required()
def add_comment(request, discussion_id):
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        # CommentForm should be able to handle the saving with save()
        if comment_form.is_valid():
            comment = Comment.objects.create(text=comment_form.cleaned_data['text'],
                                         poster=request.user,
                                         discussion=Discussion.objects.get(id=discussion_id))
        return redirect('view_discussion', discussion_id=discussion_id)


@login_required()
def add_discussion(request):
    discussion_form = DiscussionForm()

    if request.method == 'POST':
        discussion_form = DiscussionForm(request.POST)
        category = ''
        if discussion_form.is_valid():
            if discussion_form.cleaned_data['category']:
                category = discussion_form.cleaned_data['category'][0]
            else:
                cat = Category.objects.create(name=discussion_form.cleaned_data['category_input'])
                category= cat.id
            discussion = Discussion.objects.create(title=discussion_form.cleaned_data['title'],
                                                   text=discussion_form.cleaned_data['text'],
                                                   poster=request.user,
                                                   category=Category.objects.get(id=int(category)))
            return redirect('view_discussion', discussion.id)
    data = {'discussion_form':discussion_form,
            'discussionactive':'active'}
    return render(request, 'discussion/add_discussion.html', data)
