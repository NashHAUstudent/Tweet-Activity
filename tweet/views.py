from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Tweet

def tweet(request):
    """
    Handles creating a new tweet with form submission.
    This view also handles the validation for forbidden words.
    """
    error_message = None

    if request.method == 'POST':
        # Get the form data from the POST request
        text_content = request.POST.get('text')
        image_file = request.FILES.get('image')

        try:
            # Create a new Tweet object
            new_tweet = Tweet(text=text_content, image=image_file)
            # This will automatically run the clean() method and raise a ValidationError if needed
            new_tweet.save()
            # If successful, redirect to the page that shows all tweets
            return redirect('view_tweet')
        except ValidationError as e:
            # If the validation fails, store the error message to display on the page
            # The correct way to get the message from the ValidationError is with str(e)
            error_message = str(e)

    # For GET requests or if there was a validation error,
    # render the form page with an optional error message.
    context = {
        'error_message': error_message
    }
    return render(request, 'tweet.html', context)

def view_tweet(request):
    """
    Fetches all tweets from the database and renders a template to display them.
    """
    # Fetch all the tweets, ordered by the newest first.
    all_tweets = Tweet.objects.all().order_by('-created_at')

    # Prepare the context to send to the template.
    context = {
        'tweets': all_tweets,
    }

    # Render the 'view_tweet.html' template with the list of tweets.
    return render(request, 'view_tweet.html', context)