import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-05-02
# https://www.baseball-reference.com/boxes/TOR/TOR201305020.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/05/02/347170/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-02 19:07-22:29",
        "at": "Rogers Centre, Toronto, ON",
        "att": "25,851",
        "temp": "60F, Clear",
        "wind": "14mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                37: "Mike Carp",
                3: "David Ross",
                7: "Stephen Drew",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                34: "David Ortiz",
                18: "Shane Victorino",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                11: "Clay Buchholz",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [12, "0"],
                [29, "9"],
                [16, "5"],
                [37, "3"],
                [3, "2"],
                [7, "6"],
            ],
            "bench": [
                [39, "C"],
                [34, "DH"],
                [18, "CF"],
                [23, "3B"],
            ],
            "bullpen": [63, 41, 30, 19, 52, 31, 59, 36, 22, 11],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 48,
            "roster": {
                # Lineup
                13: "Brett Lawrie",
                26: "Adam Lind",
                19: "José Bautista",
                10: "Edwin Encarnación",
                9: "J.P. Arencibia",
                53: "Melky Cabrera",
                28: "Colby Rasmus",
                1: "Emilio Bonifácio",
                66: "Munenori Kawasaki",
                # Starting pitcher
                48: "J.A. Happ",
                # Bench
                3: "Maicer Izturis",
                16: "Mark DeRosa",
                22: "Henry Blanco",
                11: "Rajai Davis",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                52: "Justin Germano",
                49: "Brad Lincoln",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [48, 62, 56, 38, 27],
            "lineup": [
                [13, "5"],
                [26, "3"],
                [19, "9"],
                [10, "0"],
                [9, "2"],
                [53, "7"],
                [28, "8"],
                [1, "4"],
                [66, "6"],
            ],
            "bench": [
                [3, "3B"],
                [16, "3B"],
                [22, "C"],
                [11, "CF"],
            ],
            "bullpen": [43, 62, 50, 56, 38, 23, 52, 49, 27, 44, 32],
        },
        "umpires": {
            "HP": "Gary Darling",
            "1B": "Paul Emmel",
            "2B": "Clint Fagan",
            "3B": "Bruce Dreckman",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: TOR #48 J.A. Happ
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b f f f")
t1.out("F9")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("f f")
t1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b b s b f f")
t1.out("F9")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. TOR #13 Brett Lawrie (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.hit(4)

# 2. TOR #26 Adam Lind (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b f")
b1.out("F9")

# 3. TOR #19 José Bautista (X - X - X)
b1.new_ab()
b1.pitch_list("f b b")
b1.hit(1)
b1.thrown_out(2, "10 DP6-4-3", 2, 46)

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b1.new_ab()
b1.pitch_list("b c")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #48 J.A. Happ
t2 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c c")
t2.hit(2)
t2.advance(4, "37 1B")

# 5. BOS #29 Daniel Nava (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b s f s")
t2.out("K")

# 6. BOS #16 Will Middlebrooks (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b f b")
t2.reach("BB")
t2.advance(2, "37 1B")
t2.advance(3, "3 BB")
t2.advance(4, "7 SF9")

# 7. BOS #37 Mike Carp (X - 12 - 16)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c c")
t2.hit(1, rbis=1)
t2.advance(2, "3 BB")
t2.advance(3, "7 SF9")

# 8. BOS #3  David Ross (X - 16 - 37)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c b b")
t2.reach("BB")
t2.error(9)
t2.advance(2, "7 E9")

# 9. BOS #7  Stephen Drew (16 - 37 - 3)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.out("SF9", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (37 - 3 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c b f b f b")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.hit(1)

# 6. TOR #53 Melky Cabrera (X - X - 9)
b2.new_ab()
b2.pitch_list("f")
b2.out("L8")

# 7. TOR #28 Colby Rasmus (X - X - 9)
b2.new_ab()
b2.pitch_list("f")
b2.out("F8")

# 8. TOR #1  Emilio Bonifácio (X - X - 9)
b2.new_ab()
b2.pitch_list("f b")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #48 J.A. Happ
t3 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.hit(2)
t3.advance(3, "15 F8")

# 3. BOS #15 Dustin Pedroia (X - 5 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f f")
t3.out("F8")

# 4. BOS #12 Mike Napoli (5 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("t s c")
t3.out("!K")

# 5. BOS #29 Daniel Nava (5 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b c b")
t3.reach("BB")
t3.thrown_out(2, "16 FC6-4", 3, 48)

# 6. BOS #16 Will Middlebrooks (5 - X - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("c b")
t3.reach("FC6-4")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b b")
b3.reach("BB")
b3.advance(2, "26 SB")
b3.advance(3, "19 BB")

# 1. TOR #13 Brett Lawrie (X - X - 66)
b3.new_ab()
b3.pitch_list("b 1 b")
b3.out("(F)P3")

# 2. TOR #26 Adam Lind (X - X - 66)
b3.new_ab(is_risp=True)
b3.pitch_list("d d c b c b")
b3.reach("BB")
b3.advance(2, "19 BB")

# 3. TOR #19 José Bautista (X - 66 - 26)
b3.new_ab(is_risp=True)
b3.pitch_list("b s b d b")
b3.reach("BB")
b3.thrown_out(2, "10 DP6-4-3", 2, 46)

# 4. TOR #10 Edwin Encarnación (66 - 26 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("b b")
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #48 J.A. Happ
t4 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b b")
t4.reach("BB")
t4.thrown_out(2, "3 DP4-6-3", 1, 48)

# 8. BOS #3  David Ross (X - X - 37)
t4.new_ab()
t4.pitch_list("b f")
t4.out("DP4-6-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b b")
t4.reach("BB")
t4.advance(2, "2 BB")
t4.advance(3, "5 BB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t4.new_ab()
t4.pitch_list("f 1 f 1 f 1 b d f b b")
t4.reach("BB")
t4.advance(2, "5 BB")

# 2. BOS #5  Jonny Gomes (X - 7 - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b b d b")
t4.reach("BB")
t4.thrown_out(2, "15 FC6-4", 3, 49)

# Pitching change (TOR): #49 Brad Lincoln replaces #48 J.A. Happ
t4.pitching_substitution(49)

# 3. BOS #15 Dustin Pedroia (7 - 2 - 5)
t4.new_ab(is_risp=True)
t4.pitch_list("c b f b")
t4.reach("FC6-4")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 5. TOR #9  J.P. Arencibia (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("G6-3")

# 6. TOR #53 Melky Cabrera (X - X - X)
b4.new_ab()
b4.pitch_list("c b s f b s")
b4.out("K")

# 7. TOR #28 Colby Rasmus (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)

# 8. TOR #1  Emilio Bonifácio (X - X - 28)
b4.new_ab()
b4.pitch_list("c f f b f b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #49 Brad Lincoln
t5 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t5.new_ab()
t5.pitch_list("b s s")
t5.out("(F)P3")

# 5. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.hit(2)
t5.advance(3, "16 G3-1")

# 6. BOS #16 Will Middlebrooks (X - 29 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("G3-1")

# 7. BOS #37 Mike Carp (29 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c s s")
t5.out("K")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b5.new_ab()
b5.pitch_list("c b c b")
b5.out("G3-1")

# 1. TOR #13 Brett Lawrie (X - X - X)
b5.new_ab()
b5.pitch_list("c s c")
b5.out("!K")

# 2. TOR #26 Adam Lind (X - X - X)
b5.new_ab()
b5.pitch_list("s s b f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #49 Brad Lincoln
t6 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t6.new_ab()
t6.pitch_list("b f b c b f b")
t6.reach("BB")
t6.advance(2, "7 WP")
t6.advance(4, "2 1B")

# 9. BOS #7  Stephen Drew (X - X - 3)
t6.new_ab()
t6.pitch_list("c b s f s")
t6.wp()
t6.out("K")

# Pitching change (TOR): #50 Steve Delabar replaces #49 Brad Lincoln
t6.pitching_substitution(50)

# 1. BOS #2  Jacoby Ellsbury (X - 3 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f b")
t6.hit(1, rbis=1)
t6.advance(2, "5 G1-3")

# 2. BOS #5  Jonny Gomes (X - X - 2)
t6.new_ab()
t6.pitch_list("c 1")
t6.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("s f")
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #46 Ryan Dempster
b6 = game.new_inning()

# 3. TOR #19 José Bautista (X - X - X)
b6.new_ab()
b6.pitch_list("b c f")
b6.out("F7")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b6.new_ab()
b6.pitch_list("c f f f f f b")
b6.out("L8")

# 5. TOR #9  J.P. Arencibia (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #50 Steve Delabar
t7 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c t b c")
t7.out("!K")

# 5. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("P6")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #46 Ryan Dempster
b7.pitching_substitution(30)

# 6. TOR #53 Melky Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c f f s")
b7.out("K")

# 7. TOR #28 Colby Rasmus (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b f b")
b7.hit(1)
b7.advance(2, "1 WP")
b7.advance(3, "13 BB")

# 8. TOR #1  Emilio Bonifácio (X - X - 28)
b7.new_ab(is_risp=True)
b7.pitch_list("1 c 1 c f b")
b7.wp()
b7.out("G6-3")

# 9. TOR #66 Munenori Kawasaki (X - 28 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b f b b")
b7.reach("BB")
b7.advance(2, "13 BB")

# Pitching change (BOS): #36 Junichi Tazawa replaces #30 Andrew Miller
b7.pitching_substitution(36)

# 1. TOR #13 Brett Lawrie (X - 28 - 66)
b7.new_ab(is_risp=True)
b7.pitch_list("b c d f b d")
b7.reach("BB")

# 2. TOR #26 Adam Lind (28 - 66 - 13)
b7.new_ab(is_risp=True)
b7.pitch_list("c c d d s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #27 Brett Cecil
t8 = game.new_inning()

# Pitching change (TOR): #27 Brett Cecil replaces #50 Steve Delabar
t8.pitching_substitution(27)

# 7. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 8. BOS #3  David Ross (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 9. BOS #7  Stephen Drew (X - X - 3)
t8.new_ab()
t8.pitch_list("s s f c")
t8.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - 3)
t8.new_ab()
t8.out("G2-3")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #36 Junichi Tazawa
b8.pitching_substitution(19)

# 3. TOR #19 José Bautista (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("(F)P3")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(1)

# 5. TOR #9  J.P. Arencibia (X - X - 10)
b8.new_ab()
b8.pitch_list("b s b t s")
b8.out("K")

# 6. TOR #53 Melky Cabrera (X - X - 10)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #32 Esmil Rogers
t9 = game.new_inning()

# Pitching change (TOR): #32 Esmil Rogers replaces #27 Brett Cecil
t9.pitching_substitution(32)

# 2. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("c s")
t9.hit(1)
t9.advance(2, "15 E5")
t9.advance(3, "12 DP1-4-3")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
t9.new_ab()
t9.error(5)
t9.reach("E5")
t9.thrown_out(2, "12 DP1-4-3", 1, 32)

# 4. BOS #12 Mike Napoli (X - 5 - 15)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("DP1-4-3")

# 5. BOS #29 Daniel Nava (5 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b b b b")
t9.reach("BB")

# 6. BOS #16 Will Middlebrooks (5 - X - 29)
t9.new_ab(is_risp=True)
t9.out("(F)P3")


# Bot 9th
# Pitching: BOS #52 Joel Hanrahan
b9 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #19 Koji Uehara
b9.pitching_substitution(52)

# 7. TOR #28 Colby Rasmus (X - X - X)
b9.new_ab()
b9.pitch_list("b c b f f b")
b9.hit(1)
b9.thrown_out(2, "66 DP6-4-3", 2, 52)

# Offensive change (TOR): Pinch-hitter #11 Rajai Davis replaces #1 Emilio Bonifácio, batting 8th
b9.offensive_substitution(8, 11, "PH")

# 8. TOR #11 Rajai Davis (X - X - 28)
b9.new_ab()
b9.pitch_list("b b f")
b9.out("P4")

# 9. TOR #66 Munenori Kawasaki (X - X - 28)
b9.new_ab()
b9.pitch_list("c s")
b9.out("DP6-4-3")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46, is_away_team=True)
# SV: BOS #52 Joel Hanrahan
game.save_pitcher(52, is_away_team=True)

# Loser team: TOR
# LP: TOR #48 J.A. Happ
game.losing_pitcher(48)

# print(game)
game.generate_scorecard()
