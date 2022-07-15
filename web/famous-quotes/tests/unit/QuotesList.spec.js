import { shallowMount } from '@vue/test-utils'
import QuotesList from '@/components/QuotesList.vue'

describe('QuotesList.vue', () => {
  
  it('renders quotes props when passed', () => {
    const quotes = ['quote 1', 'quote 2', 'quotes 3'];

    const wrapper = shallowMount(QuotesList, {
      props: { quotes }
    })
    
    const renderedQuotes = wrapper.findAll('li');

    for(let i = 0; i < renderedQuotes.length; i++){
      expect(renderedQuotes[i].text()).toBe(quotes[i]);
    }

  })
})
