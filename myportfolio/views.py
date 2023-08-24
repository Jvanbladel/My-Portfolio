from django.shortcuts import render


def handle_error(request, exception=None):
    # By default, set error_code to 500 (Internal Server Error)
    error_code = 500
    error_messages = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Page Not Found",
        500: "Internal Server Error",
        # Add other error codes and messages if needed
    }

    if exception:
        error_code = getattr(exception, "status_code", 500)

    error_message = error_messages.get(error_code, "Unknown Error")
    return render(
        request,
        "errors/error.html",
        {"error_code": error_code, "error_message": error_message},
        status=error_code,
    )
