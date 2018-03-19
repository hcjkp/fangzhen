class Conditioner(object):
    def __int__(self, p_conditioner, q_conditioner, t_max, t_min, t_true, state, time):
        self.p_conditioner = p_conditioner
        self.q_conditioner = q_conditioner
        self.time = time
        self.state = state
        self.t_max = t_max
        self.t_min = t_min
        self.t_true = t_true

    def ave_conditioner(self):
        ave_conditioner = self.p_conditioner
        return ave_conditioner

    def get_data(self):




