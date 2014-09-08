class ClientController(object):

steps = [handle_client_start, handle_client_enter_token, handle_client_confirm, handle_client_confirmed]

def handle():
    if request.session['step']
        current_step = request.session['step']

        if current_step > len(steps)
            error

        next_step = steps[current_step + 1]


def __handle_client_start():
    return render_template('client-start.html')

@login_required
def __handle_client_enter_token():
    return render_template('client-enter-token.html')

@login_required
def __handle_client_confirm():
    return render_template('client-confirm.html')

@login_required
def __handle_client_confirmed():
    return render_template('client-confirmed.html')


class ConveyancerController(object):

steps = [__handle_conveyancer_start,
  __handle_conveyancer_login,
  __handle_conveyancer_search,
  __handle_conveyancer_select_property,
  __handle_conveyancer_select_task,
  __handle_conveyancer_add_clients,
  __handle_conveyancer_add_client,
  __handle_conveyancer_confirm,
  __handle_conveyancer_token]

def handle():
    if request.session['step']
        current_step = request.session['step']

        if current_step > len(steps)
            error

        next_step = steps[current_step + 1]



def __handle_conveyancer_start():
    return render_template('conveyancer-start.html')

def __handle_conveyancer_login():
    return render_template('conveyancer-login.html')

@login_required
def __handle_conveyancer_search():
    return render_template('conveyancer-search.html')

@login_required
def __handle_conveyancer_select_property():
    return render_template('conveyancer-select-property.html')

@login_required
def __handle_conveyancer_select_task():
    return render_template('conveyancer-select-task.html')

@login_required
def __handle_conveyancer_add_clients():
    return render_template('conveyancer-add-clients.html')

@login_required
def __handle_conveyancer_add_client():
    return render_template('conveyancer-add-client.html')

@login_required
def __handle_conveyancer_confirm():
    return render_template('conveyancer-confirm.html')

@login_required
def __handle_conveyancer_token():
    return render_template('conveyancer-token.html')
