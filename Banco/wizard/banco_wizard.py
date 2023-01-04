from odoo import api, models, fields


class BancoWizard(models.TransientModel):
    _name = "banco.wizard"

    teste = fields.Char()

    def butao(self):
        pagamentos = self.env['account.payment'].search([], order="id asc")
        i = len(pagamentos)

        pagamentos[i - 1].action_post()
        pagamentos[i - 2].action_post()

        a1 = pagamentos[i - 1]
        a2 = pagamentos[i - 2]

        # valor = self.currency_valor
        # valor_final = 'valor do pagamento R$' + str(valor)


        vals_list3 = {'status': 'aberto',
                      'private_message': 'public',
                      'department_id': 3,  # required
                      'user_requested_id': False,
                      'users_views_ids': [[6, False, []]],
                      'department_views_ids': [[6, False, [1, 2, 3]]],
                      'category_parent_request_id': 1,  # required
                      'category_child_request': 2,  # required
                      'boolean_client': False,
                      'request_client_ids': [[6, False, []]],
                      'description_problem': 'Transação',  # required
                      'my_requests': [[6, False, []]],
                      'message_follower_ids': [],
                      'activity_ids': [],
                      'message_ids': [],
                      'tr': [a1.id, a2.id],
                      }

        self.env['project_request'].create(vals_list3)
