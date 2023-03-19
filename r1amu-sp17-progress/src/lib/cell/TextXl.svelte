<script>
    let className;
    export { className as class };
</script>

<p class="c {className}">
    <slot />
</p>

<style lang="postcss" module>
    .c {
        @apply text-xl;
    }
</style>
