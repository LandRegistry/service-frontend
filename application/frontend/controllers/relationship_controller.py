from flask import session
from flask.ext.login import login_required
from application import app

class ClientController(object):

    def handle_client_start():
        return 'client-start.html'

    def handle_client_enter_token():
        return 'client-enter-token.html'

    def handle_client_confirm():
        return 'client-confirm.html'

    def handle_client_confirmed():
        return 'client-confirmed.html'

    global steps
    steps = [handle_client_start, handle_client_enter_token, handle_client_confirm, handle_client_confirmed]

    def handle(self, session):
        next_step_number = 0
        next_step_function = steps[0]

        try:
            if 'client_step' in session:
                current_step_number = session['client_step']
                app.logger.info(current_step_number)
                if current_step_number + 1 > len(steps):
                    raise Exception("Requested a step that does not exist")

                next_step_function = steps[current_step_number + 1]
                next_step_number = next_step_number + 1
        except KeyError:
            next_step_number = 0
            next_step_function = steps[0]
        finally:
            session['client_step'] = next_step_number
            app.logger.info("session STEP: %s" % session['client_step'])
            return next_step_function()

class ConveyancerController(object):

    def handle_conveyancer_start():
        return 'conveyancer-start.html'

    def handle_conveyancer_login():
        return 'conveyancer-login.html'

    def handle_conveyancer_search():
        return 'conveyancer-search.html'

    def handle_conveyancer_select_property():
        return 'conveyancer-select-property.html'

    def handle_conveyancer_select_task():
        return 'conveyancer-select-task.html'

    def handle_conveyancer_add_clients():
        return 'conveyancer-add-clients.html'

    def handle_conveyancer_add_client():
        return 'conveyancer-add-client.html'

    def handle_conveyancer_confirm():
        return 'conveyancer-confirm.html'

    def handle_conveyancer_token():
        return 'conveyancer-token.html'

    global steps
    steps = [handle_conveyancer_start,
      handle_conveyancer_login,
      handle_conveyancer_search,
      handle_conveyancer_select_property,
      handle_conveyancer_select_task,
      handle_conveyancer_add_clients,
      handle_conveyancer_add_client,
      handle_conveyancer_confirm,
      handle_conveyancer_token]

    def handle(self, session):
        next_step_number = 0
        next_step_function = steps[0]

        try:
            if 'conveyancer_step' in session:
                current_step_number = session['conveyancer_step']
                app.logger.info(current_step_number)
                if current_step_number + 1 > len(steps):
                    raise Exception("Requested a step that does not exist")

                next_step_function = steps[current_step_number + 1]
                next_step_number = next_step_number + 1
        except KeyError:
            next_step_number = 0
            next_step_function = steps[0]
        finally:
            session['conveyancer_step'] = next_step_number
            app.logger.info("session STEP: %s" % session['conveyancer_step'])
            return next_step_function()
