from flask.ext.login import login_required

class ClientController(object):

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


class ConveyancerController(object):

    def handle_conveyancer_start():
        return render_template('conveyancer-start.html')

    def handle_conveyancer_login():
        return render_template('conveyancer-login.html')

    @login_required
    def handle_conveyancer_search():
        return render_template('conveyancer-search.html')

    @login_required
    def handle_conveyancer_select_property():
        return render_template('conveyancer-select-property.html')

    @login_required
    def handle_conveyancer_select_task():
        return render_template('conveyancer-select-task.html')

    @login_required
    def handle_conveyancer_add_clients():
        return render_template('conveyancer-add-clients.html')

    @login_required
    def handle_conveyancer_add_client():
        return render_template('conveyancer-add-client.html')

    @login_required
    def handle_conveyancer_confirm():
        return render_template('conveyancer-confirm.html')

    @login_required
    def handle_conveyancer_token():
        return render_template('conveyancer-token.html')

    steps = [handle_conveyancer_start,
      handle_conveyancer_login,
      handle_conveyancer_search,
      handle_conveyancer_select_property,
      handle_conveyancer_select_task,
      handle_conveyancer_add_clients,
      handle_conveyancer_add_client,
      handle_conveyancer_confirm,
      handle_conveyancer_token]

    def handle():
        if request.session['step']
            current_step = request.session['step']

            if current_step > len(steps)
                error

            next_step = steps[current_step + 1]
