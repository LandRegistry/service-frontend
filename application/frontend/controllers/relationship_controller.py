from flask.ext.login import login_required

class RelationshipController(object):

    def handle_client_start():
        return render_template('client-start.html')

    @login_required
    def handle_client_enter_token():
        return render_template('client-enter-token.html')

    @login_required
    def handle_client_confirm():
        return render_template('client-confirm.html')

    @login_required
    def handle_client_confirmed():
        return render_template('client-confirmed.html')

    steps = [handle_client_start, handle_client_enter_token, handle_client_confirm, handle_client_confirmed]

    def handle():
        if request.session['step']:
            current_step = request.session['step']

            if current_step > len(steps):
                error

            next_step = steps[current_step + 1]
