from ._libdeepjets import generate_pythia as _generate
import os

def generate(config, nevents,
             random_seed=0,
             beam_ecm=13000.,
             eta_max=5.,
             jet_size=0.6, subjet_size=0.3,
             jet_pt_min=12.5, subjet_pt_min=0.05,
             cut_on_pdgid=0, pt_min=-1, pt_max=-1):
    xmldoc = os.path.join(os.environ.get('DEEPJETS_SFT_DIR', '/usr/local'),
                          'share/Pythia8/xmldoc')
    for event in _generate(config, xmldoc, nevents,
                           random_seed=random_seed,
                           beam_ecm=beam_ecm,
                           eta_max=eta_max,
                           jet_size=jet_size, subjet_size=subjet_size,
                           jet_pt_min=jet_pt_min, subjet_pt_min=subjet_pt_min,
                           cut_on_pdgid=cut_on_pdgid,
                           pt_min=pt_min, pt_max=pt_max):
        yield event
