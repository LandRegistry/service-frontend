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
        app.logger.info(" ****** YO *******")
        next_step_number = 0
        next_step_function = steps[0]

        app.logger.info("session STEP: %s" % session['step'])
        app.logger.info(" ****** YOLO *******")
        try:
            if 'step' in session:
                app.logger.info("********** IN IF *******")
                current_step_number = session['step']
                app.logger.info(current_step_number)
                if current_step_number + 1 > len(steps):
                    raise Exception("Requested a step that does not exist")

                app.logger.info("********** IN IF step 2*******")
                next_step_function = steps[current_step_number + 1]
                app.logger.info("********** IN IF step 3 *******")
                next_step_number = next_step_number + 1
                app.logger.info("********** IN IF step 4 *******")
                app.logger.info("next_step_number : %s" % next_step_number )
        except KeyError:
            app.logger.info("******** KEY ERROR ***********")
            next_step_number = 0
            next_step_function = steps[0]
        finally:
            app.logger.info(" ****** KTHNXBAI *******")
            session['step'] = next_step_number
            app.logger.info("session STEP: %s" % session['step'])
            return next_step_function()

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

    def handle(self):
        if request.session['step']:
            current_step = request.session['step']

            if current_step > len(steps):
                error

            next_step = steps[current_step + 1]
