def download_csv(subject):

    download_dir = '%s_%s_%s.csv' % (subject.get_id(), subject.get_name()[0], subject.get_name()[1])
    csv = open(download_dir, "w")

    titleRow = 'id, first_name, last_name, shape, color, music, delay_time, reaction_time, x_pos, y_pos,var, trial\n'
    csv.write(titleRow)

    vars = subject.variations
    for i in range(1,4):
        trials = vars[i].trials
        for j in range(1,6):
            temp = trials[j]

        row = '%s, %s, %s, %d, %d, %d, %d %d, %d, %d, %d, %d\n' % (subject.get_id, subject.first_name, subject.last_name,
                                                                 vars[i].shape, vars[i].color, vars[i].music,
                                                                 temp.delay_time, temp.reaction_time, temp.x_pos,
                                                                 temp.y_pos, i, j)

