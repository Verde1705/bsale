import sendgrid


class EmailReport(object):

    @staticmethod
    def sendEmail(to, subject, message, ffrom="Loadingplay <contacto@loadingplay.com>"):
        try:
            sg = sendgrid.SendGridClient("nailuj41", "Equipo_2112")

            msg = sendgrid.Mail()
            msg.add_to(to)
            msg.set_subject(subject)
            msg.set_html(message)
            msg.set_from(ffrom)

            status, msg = sg.send(msg)
        except Exception, e:
            print str(e)
