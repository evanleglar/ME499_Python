#!/usr/bin/env python3


from subprocess import check_output
import os


class Grader(object):
    def __init__(self):
        # Figure out the grading functions
        self.names = [f for f in dir(self) if f[0:6] =='grade_']
        self.func = map(lambda x: getattr(self, x), self.names)
        self.names = [name[6:] for name in self.names]
                        

    def do_grading(self):
        possible = 0
        total = 0
        for f,n in zip(self.func, self.names):
            print('Grading {0}:'.format(n))
            try:
                t,p = f()
                total += t
                possible += p
            except Exception as e:
                print('  could not grade this question')
                print('Error {}'.format(e))
                return
        score = total / possible * 100.0
        
        print('Got {0} total points out of a possible {1}, for {2:.2f}%'.format(total, possible, score))

        return score

    def output_matches(self, command, expected):
        return check_output(command.split()).decode('UTF-8') == expected


class Lab0(Grader):
    # Annoyingly, the newline conventions are different on Windows and non-Windows systems
    newline = '\r\n' if os.name == 'nt' else '\n'

    def grade_Q1(self):
        if self.output_matches('python hello.py', 'Hello, World!{0}'.format(Lab0.newline)):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1
    
    def grade_Q2(self):
        if self.output_matches('python cylinder.py', '141.3716694115407{0}'.format(Lab0.newline)):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1

    def grade_Q3(self):
        if self.output_matches('python torus.py', '17.271807701906376{0}'.format(Lab0.newline)):
            print('  passed')
            grade = 1
        else:
            print('  failed')
            grade = 0
        return grade,1

    
if __name__ == '__main__':
    g = Lab0()
    g.do_grading()

