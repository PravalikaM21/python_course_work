class Status2015:
    def view(self):
        print("You can view status")
    def reply(self):
        print("You can reply")
    def caption(self):
        print("You can add caption")

class Status2020(Status2015):
    def uploadImg(self):
        print("You can upload Image")
    def uploadVid(self):
        print("You can upload video -30 sec")
    def privacy(self):
        print("You can select who can see your status")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy")
    def reaction(self):
        print("You can send reactions")           
    def like(self):
        print("You can like the status")


class Status2024(Status2020):
    def statusrings(self):
        print("Color is added to the status display")
    def mute(self):
        print("You can mute the other's status")
    def filters(self):
        print("You can filters")

    
class Status2025(Status2023,Status2024):
    def music(self):
        print("You can add music")
    def mention(self):
        print("You can mention them")
    def collab(self):
        print("You can share your status from insta or fb")
    def voicenote(self):
        print("You can voice note")


print("\nSheshu")       
sheshu= Status2015()
sheshu.view()
sheshu.reply()
sheshu.caption()

print("\nHemanth")
hemanth=Status2020()
hemanth.uploadImg()
hemanth.uploadVid()
hemanth.privacy()
hemanth.view()
hemanth.reply()
hemanth.caption()

print("\nRasool")
rasool=Status2023()
rasool.uploadImg()
rasool.uploadVid()
rasool.privacy()
rasool.view()
rasool.reply()
rasool.caption()
rasool.ProfilePrivacy()
rasool.reaction()
rasool.like()

print("\nTarit")
tarit=Status2024()
tarit.uploadImg()
tarit.uploadVid()
tarit.privacy()
tarit.view()
tarit.reply()
tarit.caption()
tarit.statusrings()
tarit.mute()
tarit.filters()


print('\nVarun')
varun=Status2025()
varun.uploadImg()
varun.uploadVid()
varun.privacy()
varun.view()
varun.reply()
varun.caption()
varun.statusrings()
varun.mute()
varun.filters()
varun.ProfilePrivacy()
varun.reaction()
varun.like()

