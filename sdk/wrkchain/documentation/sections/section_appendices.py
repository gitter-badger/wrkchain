from string import Template

from wrkchain.documentation.sections.doc_section import DocSection


class SectionAppendices(DocSection):
    def __init__(self, section_number, title, wrkchain_name, mainchain_rpc_uri,
                 oracle_write_frequency):
        path_to_md = 'appendices.md'
        DocSection.__init__(self, path_to_md, section_number, title)

        self.__section_number = section_number
        self.__sub_section_number = 1
        self.__wrkchain_name = wrkchain_name
        self.__mainchain_rpc_uri = mainchain_rpc_uri
        self.__oracle_write_frequency = oracle_write_frequency

    def generate(self):

        appendix_1 = self.__appendix_1()
        appendix_2 = self.__appendix_2()
        appendix_3 = self.__appendix_3()
        appendix_4 = self.__appendix_4()

        d = {
            '__APPENDIX_1__': appendix_1,
            '__APPENDIX_2__': appendix_2,
            '__APPENDIX_3__': appendix_3,
            '__APPENDIX_4__': appendix_4,
        }
        self.add_content(d, append=False)
        return self.get_contents()

    def __appendix_1(self):
        appendix_md = f'{self.template_dir()}/sub/appendices/appendix1.md'
        appendix_md_path = self.root_dir / appendix_md
        appendix = appendix_md_path.read_text()
        t = Template(appendix)
        contents = t.substitute(
            {'__SECTION_NUMBER__': self.__section_number,
             '__SUB_SECTION_NUMBER__': self.__sub_section_number})
        self.__sub_section_number += 1
        return contents

    def __appendix_2(self):
        appendix_md = f'{self.template_dir()}/sub/appendices/appendix2.md'
        appendix_md_path = self.root_dir / appendix_md
        appendix = appendix_md_path.read_text()
        t = Template(appendix)
        contents = t.substitute(
            {'__SECTION_NUMBER__': self.__section_number,
             '__SUB_SECTION_NUMBER__': self.__sub_section_number})
        self.__sub_section_number += 1
        return contents

    def __appendix_3(self):
        appendix_md = f'{self.template_dir()}/sub/appendices/appendix3.md'
        appendix_md_path = self.root_dir / appendix_md
        appendix = appendix_md_path.read_text()
        t = Template(appendix)
        contents = t.substitute(
            {'__SECTION_NUMBER__': self.__section_number,
             '__SUB_SECTION_NUMBER__': self.__sub_section_number,
             '__MAINCHAIN_WEB3_PROVIDER_URL__': self.__mainchain_rpc_uri,
             '__WRKCHAIN_NAME__': self.__wrkchain_name,
             '__ORACLE_WRITE_FREQUENCY__': self.__oracle_write_frequency
             })
        self.__sub_section_number += 1
        return contents

    def __appendix_4(self):
        appendix_md = f'{self.template_dir()}/sub/appendices/appendix4.md'
        appendix_md_path = self.root_dir / appendix_md
        appendix = appendix_md_path.read_text()
        t = Template(appendix)
        contents = t.substitute(
            {'__SECTION_NUMBER__': self.__section_number,
             '__SUB_SECTION_NUMBER__': self.__sub_section_number})
        self.__sub_section_number += 1
        return contents


class SectionAppendicesBuilder:
    def __init__(self):
        self.__instance = None

    def __call__(self, section_number, title, wrkchain_name, mainchain_rpc_uri,
                 oracle_write_frequency, **_ignored):
        if not self.__instance:
            self.__instance = SectionAppendices(section_number, title,
                                                wrkchain_name,
                                                mainchain_rpc_uri,
                                                oracle_write_frequency)

        return self.__instance