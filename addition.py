 for line in datafile:
            items = line.split()

            if int(items[1]) == 0:
                continue

                if items[2] != 'NaN':
                    if self.tmplist != []:

                        for i in range(len(items)):
                            self.tmplist[i] /= self.count

                        self.data.append(self.tmplist)
                        self.tmplist = []
                        self.HR = True

                    for item in items:
                        self.tmplist.append(float(item))

                    self.count = 1


            elif self.HR:
                self.count += 1

                for i in range(3,len(items)):
                    self.tmplist[i] += float(items[i])
