from jenkinsapi.jenkins import Jenkins
class JenkinsBuild(object):
  def __init__(self, job_name):
    self.j = Jenkins('http://*********', '*****', '*****')

  def build(self):

    self.j.build_job(self.jobame, )
  def overwrite_vars(self, **kwargs):
    pass

  def invoke(self):
    self.j.build_job('InboundLogistics', params = {"PlatformType":"MonoTouch", "OutputDir":"builds", "version":"test", "CONFIGS_ROOT":"/Developer/Mediawire/MediawireConfigurations", "config":"InboundLogistics", "branch_name":"ios_012400_locked", "BuildTarget":"Live:Testing"})

JenkinsBuild('InboundLogistics').invoke()
